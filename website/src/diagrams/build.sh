#!/bin/bash
# TikZ 다이어그램 빌드 스크립트
# 사용법: ./build.sh [chNN]  (예: ./build.sh ch07)
# 인수 없으면 전체 빌드

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_BASE="$SCRIPT_DIR/../../public/img"

build_chapter() {
  local ch="$1"
  local srcdir="$SCRIPT_DIR/$ch"
  local outdir="$OUT_BASE/$ch"

  if [ ! -d "$srcdir" ]; then
    echo "ERROR: $srcdir not found"
    return 1
  fi

  mkdir -p "$outdir"

  for tex in "$srcdir"/*.tex; do
    [ -f "$tex" ] || continue
    local name=$(basename "${tex%.tex}")
    echo "  Building $ch/$name..."

    (cd "$srcdir" && pdflatex -interaction=nonstopmode "$name.tex" > /dev/null 2>&1)

    if [ -f "$srcdir/$name.pdf" ]; then
      pdftocairo -svg "$srcdir/$name.pdf" "$outdir/$name.svg" 2>/dev/null
      echo "    -> $outdir/$name.svg"
      rm -f "$srcdir"/$name.{aux,log,pdf,dvi}
    else
      echo "    ERROR: pdflatex failed for $name.tex"
      cat "$srcdir/$name.log" | grep "^!" | head -5
    fi
  done
}

if [ -n "$1" ]; then
  echo "Building $1..."
  build_chapter "$1"
else
  echo "Building all chapters..."
  for d in "$SCRIPT_DIR"/ch*/; do
    [ -d "$d" ] || continue
    ch=$(basename "$d")
    echo "Chapter: $ch"
    build_chapter "$ch"
  done
fi

echo "Done."
