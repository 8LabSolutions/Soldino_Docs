for file in *.pdf
do
  echo $file
  perl gulpeasepdf.pl $file
  echo -e "\n"
done