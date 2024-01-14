> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-fc3-custom-container-python 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc3-custom-container-python&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc3-custom-container-python" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc3-custom-container-python&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc3-custom-container-python" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc3-custom-container-python&type=packageDownload">
  </a>
</p>

<description>

快速部署一个 Custom Container Python 的 Hello World 函数到阿里云函数计算。

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-fc/tree/V3/custom-container/python/src)

</codeUrl>
<preview>

</preview>

## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>

| 服务/业务 | 权限               |
| --------- | ------------------ |
| 函数计算  | AliyunFCFullAccess |

</service>

<remark>

</remark>

<disclaimers>

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-fc3-custom-container-python) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-fc3-custom-container-python) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-fc3-custom-container-python -d start-fc3-custom-container-python`
  - 进入项目，并进行项目部署：`cd start-fc3-custom-container-python && s deploy -y`
   
</deploy>

<testEvent>
</testEvent>
