asciidoctor -a toc -a docinfo=shared -D ../output ../docs/index.adoc
mkdir -p ../output/images
cp -r ../docs/images/* ../output/images/


