# Doc Miner
A simple blockchain demo.

Doc Miner takes files as arguments and uses them to constrcut a blockchain.

Each block consists of the hash of the previous block, the document name, the hash of the document and a nonce used for mining. 

Mining autocalibrates to take at least 1 second. Mining uses SHA-256 to hash the block along with an incrementing nonce (like Bitcoin).

## Run tests
python3 -m unittest discover tests

## Usage
```
python3 -m src.doc_miner d1.txt d2.txt d3.txt
```

## Sample output

```
starting calibration...
mining block...
mining block...
mining block...

        --------------------------------------------------------------------------------
        | HEADER  : 0x0000000000000000000000000000000000000000000000000000000000000000
        | DOC_NAME: d1.txt
        | DOC_HASH: 0x3746c0ff6a6b0cd6d1f0d8fe2efab847d92bf61e002fa8910459c6406fcd3d28
        | NONCE   : 0x0000000000000000000000000000000000000000000000003a459b24244cf42f
        --------------------------------------------------------------------------------

                |
                v
        --------------------------------------------------------------------------------
        | HEADER  : 0x0000038f51e049a16f52009fd1b87a0b518b0a8beac7b3f0aa915a753261d5b2
        | DOC_NAME: d2.txt
        | DOC_HASH: 0x9988ef06650b823b7a60166f2de44ca5c6d32de15901edb6cdb4ca60e28878c9
        | NONCE   : 0x0000000000000000000000000000000000000000000000001ca742f63c533e94
        --------------------------------------------------------------------------------

                |
                v
        --------------------------------------------------------------------------------
        | HEADER  : 0x000003ccbf2a5387520adaa2c71230aa00ab1e445395dae345eb9ac090266023
        | DOC_NAME: d3.txt
        | DOC_HASH: 0x0bc6a9110661a7ea5cded240b56ad311667ece821c944843b5e11deb60ba6e16
        | NONCE   : 0x00000000000000000000000000000000000000000000000006b0d08098301937
        --------------------------------------------------------------------------------

                |
                v
```
