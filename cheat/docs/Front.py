from docs.base import Base

class Front(Base):

    _doc = {
        "npm": """
npm config set prefix "D:\\nodejs\\node_global"
npm config set cache  "D:\\nodejs\\node_cache"
npm config set registry https://registry.npm.taobao.org

npm install cnpm -g

npm run dev
""",
        "vue": """
npm install --global vue-cli
vue init webpack project-name
""",
    }
