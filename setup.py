from setuptools import setup

setup(
    name="cdn-electrum-server",
    version="0.9",
    scripts=['run_cdn_electrum_server','cdn-electrum-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'cdnelectrumserver':'src'
        },
    py_modules=[
        'cdnelectrumserver.__init__',
        'cdnelectrumserver.utils',
        'cdnelectrumserver.storage',
        'cdnelectrumserver.deserialize',
        'cdnelectrumserver.networks',
        'cdnelectrumserver.blockchain_processor',
        'cdnelectrumserver.server_processor',
        'cdnelectrumserver.processor',
        'cdnelectrumserver.version',
        'cdnelectrumserver.ircthread',
        'cdnelectrumserver.stratum_tcp',
        'cdnelectrumserver.stratum_http'
    ],
    description="Canada eCoin Electrum Server",
    author="Jason (koad) Zvaniga",
    author_email="jason@kingodalldata.com",
    license="GNU Affero GPLv3",
    url="https://github.com/koad/cdn-electrum-server/",
    long_description="""Lightweight wallet server for the Canada eCoin"""
)


