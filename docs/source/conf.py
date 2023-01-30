# -*- coding: utf-8 -*-
import sphinx_rtd_theme


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx_markdown_tables',
    # 'jaraco.packaging.sphinx',
]

# 项目信息
project = '亚声威格技术文档'
copyright = '2023, 亚声威格IT技术部'
author = '亚声威格IT技术部'
version = '1.0'
release = '1.0'
language = 'zh-CN'

#  角色
default_role = 'any'



#  入口
templates_path = ['_templates']
source_suffix = {'.rst': 'restructuredtext','.md': 'markdown'}
master_doc = 'index'


# Include Python intersphinx mapping to prevent failures
extensions += ['sphinx.ext.intersphinx']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Preserve authored syntax for defaults
autodoc_preserve_defaults = True

intersphinx_mapping.update({
    'pip': ('https://pip.pypa.io/en/latest', None),
    'build': ('https://pypa-build.readthedocs.io/en/latest', None),
    'PyPUG': ('https://packaging.python.org/en/latest/', None),
    'packaging': ('https://packaging.pypa.io/en/latest/', None),
    'twine': ('https://twine.readthedocs.io/en/stable/', None),
    'importlib-resources': (
        'https://importlib-resources.readthedocs.io/en/latest', None
    ),
})


# Support tooltips on references
extensions += ['hoverxref.extension']
hoverxref_auto_ref = True
hoverxref_intersphinx = [
    'python',
    'pip',
    'build',
    'PyPUG',
    'packaging',
    'twine',
    'importlib-resources',
]


# Add support for linking usernames
github_url = 'https://github.com'
github_repo_org = 'pypa'
github_repo_name = 'setuptools'
github_repo_slug = f'{github_repo_org}/{github_repo_name}'
github_repo_url = f'{github_url}/{github_repo_slug}'
github_sponsors_url = f'{github_url}/sponsors'


# 链接扩展
extensions += ['sphinx.ext.extlinks']
extlinks = {
    'user': (f'{github_sponsors_url}/%s', '@%s'),  # noqa: WPS323
    'pypi': ('https://pypi.org/project/%s', '%s'),  # noqa: WPS323
    'wiki': ('https://wikipedia.org/wiki/%s', '%s'),  # noqa: WPS323
}




# 重定向
# extensions += ['sphinx_reredirects']
# redirects = {
#     "userguide/keywords": "/deprecated/changed_keywords.html",
#     "userguide/commands": "/deprecated/commands.html",
# }

# Add support for inline tabs
extensions += ['sphinx_inline_tabs']



# HTML 主题


html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
        # 'analytics_anonymize_ip': False,
        # 'logo_only': False,
        # 'display_version': True,
        # 'prev_next_buttons_location': 'bottom',
        # 'style_external_links': False,
        # 'vcs_pageview_mode': '',
        # 'style_nav_header_background': 'white',
        # # Toc options
        # 'collapse_navigation': True,
        'sticky_navigation': True,
        'navigation_depth': 4,
        # 'includehidden': True,
        # 'titles_only': False
    }
# html_logo = "_static/yswg_logo.png"
# html_theme = 'furo'
# html_theme_options = {
#     "sidebar_hide_name": True,
#     "light_css_variables": {
#         "color-brand-primary": "#336790",  # "blue"
#         "color-brand-content": "#336790",
#     },
#     "dark_css_variables": {
#         "color-brand-primary": "#E5B62F",  # "yellow"
#         "color-brand-content": "#E5B62F",
#     },
# }






# Support for distutils

# Ref: https://stackoverflow.com/a/30624034/595220
nitpick_ignore = [
    ('c:func', 'SHGetSpecialFolderPath'),  # ref to MS docs
    ('envvar', 'DISTUTILS_DEBUG'),  # undocumented
    ('envvar', 'HOME'),  # undocumented
    ('envvar', 'PLAT'),  # undocumented
    ('envvar', 'DIST_EXTRA_CONFIG'),  # undocumented
    ('py:attr', 'CCompiler.language_map'),  # undocumented
    ('py:attr', 'CCompiler.language_order'),  # undocumented
    ('py:class', 'distutils.dist.Distribution'),  # undocumented
    ('py:class', 'distutils.extension.Extension'),  # undocumented
    ('py:class', 'BorlandCCompiler'),  # undocumented
    ('py:class', 'CCompiler'),  # undocumented
    ('py:class', 'CygwinCCompiler'),  # undocumented
    ('py:class', 'distutils.dist.DistributionMetadata'),  # undocumented
    ('py:class', 'FileList'),  # undocumented
    ('py:class', 'IShellLink'),  # ref to MS docs
    ('py:class', 'MSVCCompiler'),  # undocumented
    ('py:class', 'OptionDummy'),  # undocumented
    ('py:class', 'UnixCCompiler'),  # undocumented
    ('py:exc', 'CompileError'),  # undocumented
    ('py:exc', 'DistutilsExecError'),  # undocumented
    ('py:exc', 'DistutilsFileError'),  # undocumented
    ('py:exc', 'LibError'),  # undocumented
    ('py:exc', 'LinkError'),  # undocumented
    ('py:exc', 'PreprocessError'),  # undocumented
    ('py:exc', 'setuptools.errors.PlatformError'),  # sphinx cannot find it
    ('py:func', 'distutils.CCompiler.new_compiler'),  # undocumented
    # undocumented:
    ('py:func', 'distutils.dist.DistributionMetadata.read_pkg_file'),
    ('py:func', 'distutils.file_util._copy_file_contents'),  # undocumented
    ('py:func', 'distutils.log.debug'),  # undocumented
    ('py:func', 'distutils.spawn.find_executable'),  # undocumented
    ('py:func', 'distutils.spawn.spawn'),  # undocumented
    # TODO: check https://docutils.rtfd.io in the future
    ('py:mod', 'docutils'),  # there's no Sphinx site documenting this
]

# Allow linking objects on other Sphinx sites seamlessly:
intersphinx_mapping.update(
    python=('https://docs.python.org/3', None),
)

# Add support for the unreleased "next-version" change notes
# extensions += ['sphinxcontrib.towncrier']
# # Extension needs a path from here to the towncrier config.
# towncrier_draft_working_directory = '..'
# # Avoid an empty section for unpublished changes.
# towncrier_draft_include_empty = False

# extensions += ['jaraco.tidelift']

# Add icons (aka "favicons") to documentation
html_static_path = ['_static'] 
extensions += ['sphinx-favicon']
 # should contain the folder with icons

# List of dicts with <link> HTML attributes
# static-file points to files in the html_static_path (href is computed)
favicons = [
    {  # "Catch-all" goes first, otherwise some browsers will overwrite
        "rel": "icon",
        "type": "image/svg+xml",
        "static-file": "_static/yswg_logo.png",
        "sizes": "any"
    },
    {  # Version with thicker strokes for better visibility at smaller sizes
        "rel": "icon",
        "type": "image/svg+xml",
        "static-file": "_static/yswg_logo.png",
        "sizes": "16x16 24x24 32x32 48x48"
    },
    # rel="apple-touch-icon" does not support SVG yet
]



# Add support for nice Not Found 404 pages
# extensions += ['notfound.extension']