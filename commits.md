# Commit Convention
This markdown file addresses how commits should be formatted, should collaboration occur and for general good practice.

## Commit messages
Commit messages are anything in the primary 'Update ...' box in github.com
or anything that is listed __on__ the first line of the text editor in the local
Git vct.

### For a commit that addresses only one change:
type(scope): change
 > Will typically be in the present tense (not past!)

### For a commit that addresses multiple changes under the same type:
type(scope): change one; change two
 > Scope must be the more significant change commited.

## Commit Descriptions
Commit descriptions are anything in the box below the 'Update ...' box in github.com
or anything that is listed __below__ the first line of the text editor in the local
Git vct.

### All commits
All commits must include a short list of changes, going into more detail regarding the
purpose and effect of the changes to be commited to the repo.

 - Refactor variable 'foo' to 'bar' for readability
 - Refactor function 'baz' to 'foo' for compatability with 'bar'
 > *This is an example substitute for a commit scenario
