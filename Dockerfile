# 获取sphinx镜像, 下载相关依赖
FROM sphinxdoc/sphinx AS builder
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install --upgrade pip
RUN pip install sphinx-hoverxref jaraco.packaging sphinx-rtd-theme furo recommonmark sphinx_markdown_tables sphinx-inline-tabs sphinx-favicon

# 构建
COPY ./docs /docs/
WORKDIR /docs
RUN make html


# 打包编译后文件到nginx下
FROM nginx:alpine
COPY --from=builder /docs/build/html/. /usr/share/nginx/html/
