ls -a;
git add v1;
git add v2;
git add base;
git status;
git merge-file v1 base v2 -p;
echo "goodbye";
git status;
