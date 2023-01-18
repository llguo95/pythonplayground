# Description

*Insert information about the pull request features, list of improvements and bugfixes.*


# Checklist

The steps in this checklist describe the minimum set of tasks required for pull request approval and merging.

The work is divided between **assignees** and **reviewers**, as described in each point. Check this [link](https://github.com/CM2S/LINKS/wiki/List-of-PR-Reviewers) to guide your reviewers choice.

Unless otherwise explicitly stated, **all steps in this list must be done sequentially**.
If any modification is required or requested by one of the reviewers during this process, guidance is given to ensure testing and reviewing are not compromised.


### 1. Pull request creation
  To be completed by **assignees**. These tasks must be completed before assigning the work to reviewers.
  - [ ] Complete the PR description and list of improvements and bugfixes

### 2. Automatic checks
  - Make sure that the automated checks pass

### 2. Code Review
  **Reviewers** must carry the following tasks **individually**. If any point requires modifications, **undo all progress and return to step 1**.
  - [ ] Check that `LINKS` can be built with all compilers (use `make test_builds` to try all possibilities):
    - [ ] *Single-scale* version: `gfortran`,  `ifort` and `nagfor`
    - [ ] *Coupled multi-scale* version: `gfortran`,  `ifort`
  - [ ] Check that the documentation can be successfully generated with `ford`
  - [ ] Peer code review (verify new code organisation quality and appropriate comments):
  - [ ] Validate PR description and lists of improvements and bugfixes
  - [ ] Check that Datafiles have been updated with the new keywords (branch `master` of [utilities](https://github.com/CM2S/Utilities))
  - [ ] Check that appropriate new examples have been added to the branch `master` of [cr](https://github.com/CM2S/LINKS-CR)


### 3. Regression testing
  Once all code and sundry changes are reviewed, **reviewers** must run [LINKS' testing script](https://github.com/CM2S/LINKS-CR/blob/master/LINKS-CR.sh) for regression testing.
  To ease testing workflow, these tasks _can be done in parallel_ and should be divided among reviewers.
  As before, if any point fails and requires modifications, **undo all progress and return to step 1**.
  - [ ] Release mode:
    - [ ] Using `gfortran`:
      - [ ] Single macro-scale examples
      - [ ] Single micro-scale examples
      - [ ] Coupled multi-scale examples
      - [ ] Coupled multi-scale examples (forced domain decomposition)
    - [ ] Using `ifort`:
      - [ ] Single macro-scale examples
      - [ ] Single micro-scale examples
      - [ ] Coupled multi-scale examples
      - [ ] Coupled multi-scale examples (forced domain decomposition)
    - [ ] Using `nagfor`:
      - [ ] Single macro-scale fast examples
      - [ ] Single micro-scale fast examples
  - [ ] Debug mode:
    - [ ] Using `gfortran`:
      - [ ] Single macro-scale fast examples
      - [ ] Single micro-scale fast examples
      - [ ] Coupled multi-scale fast examples
      - [ ] Coupled multi-scale fast examples (forced domain decomposition)
    - [ ] Using `ifort`:
      - [ ] Single macro-scale fast examples
      - [ ] Single micro-scale fast examples
      - [ ] Coupled multi-scale fast examples
      - [ ] Coupled multi-scale fast examples (forced domain decomposition)
    - [ ] Using `nagfor`:
      - [ ] Single macro-scale fast examples
      - [ ] Single micro-scale fast examples
  - [ ] Cross verify between **assignees** and **reviewers** that all tests pass


### 4. Prepare to merge
  After regression testing has passed, follow these steps to prepare the merge.
- [ ] **Assignees**: Update the [cr](https://github.com/CM2S/LINKS-CR) submodule to the commit with the added examples, by running the following commands in the LINKS root directory:
    ```
    git add cr
    git commit -m 'Updated cr submodule'
    ```
- [ ] **Assignees**: Update default dependency files using `make gen_dep` and commit all the `.depend_*` files
- [ ] **Assignees**: Update LINKS's version by mannually updating the `.VERSION` file with the appropriate version identifier
- [ ] **Reviewers**: Approve pull request once these steps are completed


### 5. Merge
  After **all reviewers** approve the pull request, one of the **assignees** should merge the changes (**use merge squash**).


### 6. After merging
  Once the pull request is successfully merged, one of the **assignees** must archive the old branch and release a new version by:
- [ ] Create `archive/PRvX.Y.Z` tags for merged branch and push to origin:
    ```
    git tag archive/PRvX.Y.Z
    git push origin archive/PRvX.Y.Z
    ```
- [ ] Delete the merged branch
- [ ] Create the new release following the [semantic versioning](https://semver.org/) convention for version tag. Use the description (Improvements, Bugfixes, etc) as a base for the release notes. Moreover, compile the bugfixes related with the commits added since the last release