# key-project.org

Source files of the [KeY webpage](https://key-project.org), which are rendered by [hugo](https://gohugo.io). 

## GitLab CI

This project's static Pages are built by [GitLab CI][ci], following the steps
defined in [`.gitlab-ci.yml`](.gitlab-ci.yml).

## Building locally

To work locally with this project, you'll have to follow the steps below:

1. Fork, clone or download this project
1. [Install][] Hugo
1. Preview your project: `hugo server`
1. Add content
1. Generate the website: `hugo` (optional)

Read more at Hugo's [documentation][].

### Preview your site

If you clone or download this project to your local computer and run `hugo server`,
your site can be accessed under `localhost:1313/hugo/`.

The theme used is adapted from http://themes.gohugo.io/beautifulhugo/.

## GitLab User or Group Pages

To use this project as your user/group website, you will need one additional
step: just rename your project to `namespace.gitlab.io`, where `namespace` is
your `username` or `groupname`. This can be done by navigating to your
project's **Settings**.

You'll need to configure your site too: change this line
in your `config.toml`, from `"https://pages.gitlab.io/hugo/"` to `baseurl = "https://namespace.gitlab.io"`.
Proceed equally if you are using a [custom domain][post]: `baseurl = "http(s)://example.com"`.

Read more about [user/group Pages][userpages] and [project Pages][projpages].
