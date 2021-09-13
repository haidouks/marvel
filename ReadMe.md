[![CircleCI](https://circleci.com/gh/haidouks/marvel/tree/master.svg?style=svg)](https://circleci.com/gh/haidouks/marvel/tree/master)

# Marvel Search Engine
Marvel Search Engine is a python cli which takes a keyword from user and finds related marvel characters

## How to start ?

 - Easiest way to start marvel search engine is docker run. 
 - Search engine container accepts 3 environment variables which you should get them from [marvel developer portal](https://developer.marvel.com/account)
     - marvel_api
     - marvel_public_key
     - marvel_private_key

```Powershell
♥ pwsh::marvel$ docker run -it --rm  -e marvel_api="https://gateway.marvel.com:443" -e marvel_public_key="**************" -e marvel_private_key="**************" cnsn/marvel:latest
Please enter a keyword: _
```

## Development
- If you want to develop this project you can build and run your own container

```Powershell
♥ pwsh::marvel$ docker build -t marvel-search .
♥ pwsh::marvel$ docker run -it --rm  -e marvel_api="https://gateway.marvel.com:443" -e marvel_public_key="**************" -e marvel_private_key="**************" marvel-search
```
- Also please keep in mind that there is a pre-configured launch.json file in .vscode folder which will let you to debug project. Replacing environment variables with your owns should be enough.
```json
"env": {
    "marvel_api" : "https://gateway.marvel.com:443",
    "marvel_public_key" : "********",
    "marvel_private_key" : "********"
}
```

## Testing
- After setting required environment variables tests can be started:
```Powershell
♥ pwsh::marvel$ $env:marvel_private_key = "*******"
♥ pwsh::marvel$ $env:marvel_public_key = "*******"
♥ pwsh::marvel$ $env:marvel_api = "https://gateway.marvel.com:443"
♥ pwsh::marvel$ pytest --verbose

```