#!/bin/bash

echo starting geth node:
exec geth --rpc --rpcaddr localhost --rpcport 8545 --syncmode "light"
