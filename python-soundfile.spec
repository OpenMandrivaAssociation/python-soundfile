Name:		python-soundfile
Version:	0.14.0
Release:	2
Summary:	Audio file I/O through libsndfile
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/bastibe/python-soundfile
Source0:	https://files.pythonhosted.org/packages/source/s/soundfile/soundfile-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cffi)
Requires:	python%{pyver}dist(cffi)
Requires:	python%{pyver}dist(numpy)
Requires:	python%{pyver}dist(typing-extensions)
# cffi dlopens libsndfile; ELF generator will not see it
Requires:	lib64sndfile

# Force the pep517 path. setup.py's setup_requires fetch hits a
# setuptools bug when some installed dist has name=None.
%prep -a
cat > pyproject.toml <<'EOF'
[build-system]
requires = ["setuptools", "cffi>=1.0"]
build-backend = "setuptools.build_meta"
EOF

%description
soundfile reads and writes WAV/FLAC/OGG via the system libsndfile.
Used by ACE-Step for audio export (instead of torchaudio/torchcodec).

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/soundfile.py
%{py_sitedir}/_soundfile.py
%{py_sitedir}/__pycache__/soundfile*.pyc
%{py_sitedir}/__pycache__/_soundfile*.pyc
%{py_sitedir}/soundfile-*.*-info
