FROM golang:1.21

WORKDIR /usr/src/app

COPY . .

RUN go build -o main .

EXPOSE 50051

CMD ["./main"]