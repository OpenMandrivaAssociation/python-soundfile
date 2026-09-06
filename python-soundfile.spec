Name:		python-soundfile
Version:	0.14.0
Release:	1
Summary:	Audio file I/O through libsndfile
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/bastibe/python-soundfile
Source0:	https://files.pythonhosted.org/packages/source/s/soundfile/soundfile-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cffi)
Requires:	python%{pyver}dist(cffi)
Requires:	python%{pyver}dist(numpy)
Requires:	python%{pyver}dist(typing-extensions)
# cffi dlopens libsndfile; ELF generator will not see it
Requires:	lib64sndfile

%description
soundfile reads and writes WAV/FLAC/OGG via the system libsndfile.
Used by ACE-Step for audio export (instead of torchaudio/torchcodec).

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/soundfile.py
%{py_sitedir}/_soundfile.py
%{py_sitedir}/soundfile-*.*-info
