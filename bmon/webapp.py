import pprint
import datetime
import os

from flask import Flask, request, jsonify

from bmon_infra.infra import get_hosts


app = Flask(__name__)


HOSTS = [h for h in get_hosts()[1].values() if 'bitcoin' in h.tags]


@app.route('/v0/report', methods=['POST'])
def report():
    content = request.json
    content = _deserialize_body(content)
    pprint.pprint(content)
    return jsonify({'status': 'ok'})


@app.route('/', methods=['GET'])
def home():
    return 'sup'


def _deserialize_body(content: dict):
    if 'date' in content:
        content['date'] = datetime.datetime.strptime(
            content['date'], "%Y-%m-%dT%H:%M:%SZ")

    return content


@app.route('/prom_scrape_config', methods=['GET'])
def prom_scrape_config():
    targets = [
        {
            'targets': list(filter(None, [
                f'{host.name}:{host.bitcoind_exporter_port}',
                (
                    f'{host.name}:{host.prom_exporter_port}' if
                    host.prom_exporter_port else ''
                ),
            ])),
            'labels': {
                'job': 'bitcoind',
                'bitcoin_version': host.bitcoin_version,
                'bitcoin_dbcache': host.bitcoin_dbcache,
                'bitcoin_prune': host.bitcoin_prune,
            },
        }
        for host in HOSTS
    ]
    return jsonify(targets)


def main():
    app.run(
        debug=True,
        port=os.environ.get('BMON_WEB_PORT', 8080),
        host='0.0.0.0')


if __name__ == '__main__':
    main()
