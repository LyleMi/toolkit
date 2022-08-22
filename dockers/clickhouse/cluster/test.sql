select * from system.clusters

--基于test_cluster1创建分布式表
CREATE TABLE IF NOT EXISTS user_cluster on cluster test_cluster1
(
    id Int8,
    name String
) ENGINE = Distributed(
    -- 集群名称
    test_cluster1,
    -- 数据库名称
    default,
    -- 表名称
    user_local,
    -- sharding_key：可选的，用于分片的key值，在数据写入的过程中，分布式表会依据分片key的规则，将数据分布到各个节点的本地表
    rand()
);

-- 在 ck1 / ck2 分别执行
CREATE TABLE IF NOT EXISTS user_local
(
    id Int8,
    name String
) ENGINE = MergeTree()
ORDER BY id;

INSERT INTO user_local VALUES(1,'foo'), (2,'bar');
INSERT INTO user_cluster VALUES(3,'zhangsan'), (4,'lisi');
SELECT * FROM user_cluster;
SELECT * FROM user_local;
