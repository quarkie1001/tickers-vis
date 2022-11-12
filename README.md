Docker-Tickers-Vis
---
This repository shows an example of creating a simple prototype of ticker-generating service with a 
realtime graph-building feature. The basis of the implementation is visualization by Plotly Dash, 
and Redis storafe with TimeSeries module for rapid data saving and fetching.

Branch https://github.com/quarkie1001/tickers-vis/tree/redis-ws contains 3 microservice version. It uses Websocker-server that generates tickers values and send it 
over Websocket to Redis storage.

Branch https://github.com/quarkie1001/tickers-vis/tree/redis-only uses no Websocket, and prices persisting to Redis right after generation.

Installation
---
To start a demonstration just start a docker-compose container with:
```docker-compose up```

Ru 
---
Этот репозиторий хранит прототип сервиса по ежесекундной генерации цен 100 искусственных торговых инструментов 
и веб-сервиса их визуализации.
В качестве основы реализации сервиса генерации было выбрано Redis-хранилище с модулем TimeSeries, 
как оптимально подходящее для хранения такого рода данных (временные ряды цен). 
В качестве основы веб-сервиса визуализации был выбран Plotly Dash. 

В первом прототипе (ветка https://github.com/quarkie1001/tickers-vis/tree/redis-ws) была выстроена схема с использование вебсокетов: 
микросервис генерации цен (продюсер) совмещен с вебсокет-сервером, микросервис хранения данных(консюмер) совмещен с вебсокет-клиентом.

Во второй реализации (ветка https://github.com/quarkie1001/tickers-vis/tree/redis-only) схема упрощена и после генерации, данные о ценах сразу сохраняются в хранилище Redis.

Вариант связи по стандартному HTTP/1 REST API был отброшен в виду того, что данные должны отдаваться перманентно 
и слать посекундные HTTP-запросы показалось неоптимальным. 
