#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)
if(length(args) != 1) {
  stop("Usage: Rscript --vanilla square.R <number>")
} else {
  num <- as.numeric(args[1])
  print(paste0("Number: ", num))
  print(paste0("Square: ", num^2))
}