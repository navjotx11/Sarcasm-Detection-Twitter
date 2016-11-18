
data1 <- read.csv("../../data/sarcasm_gen_features.csv")
data2 <- read.csv("../../data/sarcasm_emoji.csv")
data3 <- c(data1,data2)
write.csv(data3,file = "../../data/sarcasm_final_features.csv",row.names = FALSE)


data1 <- read.csv("../../data/nonsarcasm_gen_features.csv")
data2 <- read.csv("../../data/nonsarcasm_emoji.csv")
data3 <- c(data1,data2)
write.csv(data3,file = "../../data/nonsarcasm_final_features.csv",row.names = FALSE)

