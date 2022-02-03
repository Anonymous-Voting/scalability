# test scalibility of anonymous voting on blockchain via zether

### Pre Requisites

familiarity with Python.

### Set Up

Install the dependencies:

[Install Geth](https://geth.ethereum.org/docs/install-and-build/installing-geth)

run geth node:

```bash
$ geth --networkid 9999 --datadir "./data" --port 30303 --ipcdisable --syncmode full --http --allow-insecure-unlock --http.corsdomain "*" --http.api 'eth,net,web3' --http.port 8545 --unlock 0x8AD032E701410A62c2E2b66393680648A0352A56 --password password.txt --preload skipEmpty.js --usb --nodiscover --mine console
```

then run the:

```bash
$ python3 scalability.py
```

Now you can start making changes.
