# blockchain_demo

Simple blockchain demo written in Python.

A blockchain is constructed from hashes of documents. Mining calibrates to ~1 sec per block for host machine. Blocks are mined using SHA-256.

## Run tests
python3 -m unittest discover tests

## Sample output

```
Creating blockchain
Adjusting difficulty...
Difficulty: 24
block 1 mined...
block 2 mined...
block 3 mined...
block 4 mined...

        --------------------------------------------------------------------------------
        | HEADER  : 0x0000000000000000000000000000000000000000000000000000000000000000
        | DOC_NAME: document_1
        | DOC_HASH: 0xf28b17c428460d1ca9491000be9e03f75cc3e1af3e96c7ee9a81aefdf54b6720
        | NONCE   : 0x00000000000000000000000000000000000000000000000029be5730cccdf2da
        --------------------------------------------------------------------------------

                |
                v
        --------------------------------------------------------------------------------
        | HEADER  : 0x000000d3432aa9dc8632188106ce30a70f065adc0ea4736091156f924c8c6878
        | DOC_NAME: document_2
        | DOC_HASH: 0x84086436b6449e51a14c03542a4507bf1bf5ad405da93c39aa74897f7ea1b955
        | NONCE   : 0x0000000000000000000000000000000000000000000000000b77dac55c8ff2cb
        --------------------------------------------------------------------------------

                |
                v
        --------------------------------------------------------------------------------
        | HEADER  : 0x000001430f79e42e9837878029765a333d7c6ecdc6b52cf1c1cc66b26a0c54ef
        | DOC_NAME: document_3
        | DOC_HASH: 0x122607a199b7120f0dbc735025ef882cfdf4931eb6a1db2a16b4605b0bf2d308
        | NONCE   : 0x000000000000000000000000000000000000000000000000108c8a195bdae019
        --------------------------------------------------------------------------------

                |
                v
        --------------------------------------------------------------------------------
        | HEADER  : 0x000000766f7c787126f3351ef0a89a5ab4d884094c32549a27ecdc248c08037b
        | DOC_NAME: document_4
        | DOC_HASH: 0x83a1064d7ff5017b30b67d0aae7ce5307a45c5d221d35a82081ab974b0685f16
        | NONCE   : 0x0000000000000000000000000000000000000000000000007e37ee20577ed862
        --------------------------------------------------------------------------------

                |
                v
```
