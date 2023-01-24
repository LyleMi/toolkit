#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Kafka(Base):
    _doc = {
        "command line": """
kafka-topics.sh --bootstrap-server kafka:9092 --describe
kafka-console-producer.sh --topic topic_name --bootstrap-server kafka:9092
kafka-console-consumer.sh --topic topic_name --bootstrap-server kafka:9092 --from-beginning
"""
    }

