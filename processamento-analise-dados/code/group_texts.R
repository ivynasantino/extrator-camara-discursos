library(readr)
library(tidyverse)
library(magrittr)

file_name = "ccjc_reuniao-16-04-2019_10h.csv"

previdencia_ccjc = read_csv(paste0("data/process-data/", file_name))

filter_presidente = previdencia_ccjc %>% 
  filter(autor != "FELIPE FRANCISCHINI")

group_dep = filter_presidente %>% 
  group_by(autor, data, partido, uf) %>% 
  summarise(all_discursos = paste(unlist(t(discurso)),collapse="+"))

write_csv(group_dep, paste0("data/", file_name))
