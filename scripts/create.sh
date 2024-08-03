asciidoctor -a docinfo=shared -D ../output ../docs/*.adoc
mkdir -p ../output/images
cp -r ../docs/images/* ../output/images/


