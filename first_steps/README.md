# First-Steps on Mac


1. install python
2. Install celery 
    - `pip install celery`
3. Install RabbitMQ
    - `brew install rabbitmq-server`
4. Run RabbitMQ
    - `rabbitmq-server`
        - This will start the RabbitMQ instance running
        - https://www.rabbitmq.com/man/rabbitmq-server.1.man.html
    - `rabbitmq-server -detached`
        - Use this to run RabbitMQ in the background
    - `rabbitmqctl`
        - https://www.rabbitmq.com/man/rabbitmqctl.1.man.html
        - Used to control rabbitmq
5. Create the code
    - See tasks.py
        - Read comments
6. Run celery using the code
    - `celery -A tasks worker --loglevel=info`
        - `-A`
            - APP, --app=APP     app instance to use (e.g. module.attr_name)
            - In this case the app is the tasks.py file
        - `worker`
            - Creates a celery worker instance
        - `--loglevel=info`
            - The log level
        - This creates the worker instance to process messages that RabbitMQ receives.
7. Now run the code
    - `python`
        - This is to execute the code using RabbitMQ
    - `from tasks import add`
        - This lets you use the add function you created in tasks.py
        - This should be pointing to the RabbitMQ instance on localhost
    - `add.delay(4, 4)`
        - Sends a request to RabbitMQ that add it to its queue
        - The worker then grabs the request from the queue, performs the processing
        - The worker return the result message to RabbitMQ
8. Veriy worker ran
    - You should be able to view the celery worker's log output to see that it ran
        ```
        [2016-10-07 17:40:29,831: WARNING/MainProcess] /usr/local/lib/python2.7/site-packages/celery/apps/worker.py:161: CDeprecationWarning: 
        Starting from version 3.2 Celery will refuse to accept pickle by default.

        The pickle serializer is a security concern as it may give attackers
        the ability to execute any command.  It's important to secure
        your broker from unauthorized access when using pickle, so we think
        that enabling pickle should require a deliberate action and not be
        the default choice.

        If you depend on pickle then you should set a setting to disable this
        warning and to be sure that everything will continue working
        when you upgrade to Celery 3.2::

            CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

        You must only enable the serializers that you will actually use.


          warnings.warn(CDeprecationWarning(W_PICKLE_DEPRECATED))
         
         -------------- celery@lknecht-mbpr15 v3.1.23 (Cipater)
        ---- **** ----- 
        --- * ***  * -- Darwin-15.6.0-x86_64-i386-64bit
        -- * - **** --- 
        - ** ---------- [config]
        - ** ---------- .> app:         tasks:0x1092febd0
        - ** ---------- .> transport:   amqp://guest:**@localhost:5672//
        - ** ---------- .> results:     rpc://
        - *** --- * --- .> concurrency: 8 (prefork)
        -- ******* ---- 
        --- ***** ----- [queues]
         -------------- .> celery           exchange=celery(direct) key=celery
                        

        [tasks]
          . tasks.add

        [2016-10-07 17:40:29,965: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
        [2016-10-07 17:40:29,977: INFO/MainProcess] mingle: searching for neighbors
        [2016-10-07 17:40:30,985: INFO/MainProcess] mingle: all alone
        [2016-10-07 17:40:30,996: WARNING/MainProcess] celery@lknecht-mbpr15 ready.
        [2016-10-07 17:44:48,937: INFO/MainProcess] Received task: tasks.add[44cdc46b-dd70-462c-8e86-ebd889bab4c3]
        [2016-10-07 17:44:48,953: INFO/MainProcess] Task tasks.add[44cdc46b-dd70-462c-8e86-ebd889bab4c3] succeeded in 0.0146368540009s: 0
        ```


