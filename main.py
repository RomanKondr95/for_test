import requests as r
import json


URL = 'https://akash-api.polkachu.com/cosmos/base/tendermint/v1beta1/blocks/'


def get_txs_by_block(block_num: int) -> dict:
    response = r.get(URL + str(block_num))
    if response.status_code == 400:
        return response.json()
    elif response.status_code == 200:
        json = response.json()
        return json.get('block').get('data')
    
    return {'error': 'internal error'}


if __name__ == '__main__':
    inp = int(input('Write block number: \n'))
    print(json.dumps(get_txs_by_block(inp), indent=4))