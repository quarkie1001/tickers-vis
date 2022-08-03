Docker-Tickers-Vis
---
This repository shows an example of creating a simple prototype of ticker-generating service with a 
realtime graph-building feature. The basis of the implementation is visualization by Plotly Dash, 
and Redis storafe with TimeSeries module for rapid data saving and fetching.

This branch uses no Websocket, and prices persisting to Redis right after generation.

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

В этой реализации (ветка redis-only) схема упрощена и после генерации, данные о ценах сразу сохраняются в хранилище Redis.

Вариант связи по стандартному HTTP/1 REST API был отброшен в виду того, что данные должны отдаваться перманентно 
и слать посекундные HTTP-запросы показалось неоптимальным. 
