from docs.base import Base

class Front(Base):

    _doc = {
        "init": """
sudo apt install -y nodejs npm
sudo npm install n -g
sudo n stable
sudo n latest
""",
        "npm": """
npm config set prefix "D:\\nodejs\\node_global"
npm config set cache  "D:\\nodejs\\node_cache"
npm config set registry https://registry.npm.taobao.org
npm config set registry http://mirrors.cloud.tencent.com/npm/

npm install cnpm -g

npm run dev
""",
        "vue": """
npm install --global vue-cli
vue init webpack project-name
""",
    }
