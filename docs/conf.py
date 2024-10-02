# Copyright 2024 Gonzalo Atienza Rela
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

import nonces  # noqa: E402

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

project = nonces.__title__
copyright = nonces.__copyright__
author = nonces.__author__
release = nonces.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme"
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]
source_suffix = ".rst"
master_doc = "index"

if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"
