#!/usr/bin/env bash

# this is the bash file that make this respository auto push into master after commit
rm .git/hooks/post-commit
echo "#!/usr/bin/env bash" >> .git/hooks/post-commit
echo "git push origin master" >> .git/hooks/post-commit
echo "echo 'push into master'" >> .git/hooks/post-commit
sudo chmod -x .git/hooks/post-commit

