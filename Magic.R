rm(list=ls())

library(tidyverse)
library(jsonlite)

getwd()

data <- jsonlite::fromJSON(txt = file.path("/Users", "andrewcoogan", "Documents", "Source Control",
                                         "MagicTutor", "AllCards.json"))

names_list <- stringr::str_split(names(unlist(data)), pattern = "[.]")
unique_names <- unique(sapply(names_list,function(x) x[length(x)]))

plyr::rbind.fill(lapply(data, function(f) {
  as.data.frame(Filter(Negate(is.null), f))
}))
