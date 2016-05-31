for f in *.jpg
do
    mogrify $f -resize 2500x2500\> -quality 50 $f
done
