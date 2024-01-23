package main

import (
	"context"
	"fmt"
	"log"
	"sync"
	"time"

	pb "asyncGrpcClient/proto"
	"google.golang.org/grpc"
)

func makeRequest(client pb.GreeterClient, name string, wg *sync.WaitGroup) {
	defer wg.Done()

	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()

	r, err := client.SayHello(ctx, &pb.HelloRequest{Name: name})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Println("Greeter client received: %s", r.GetMessage())
}

func main() {
	log.Println("Starting client...")
	conn, err := grpc.Dial("python-service:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	client := pb.NewGreeterClient(conn)

	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go makeRequest(client, fmt.Sprintf("you%d", i), &wg)
	}

	wg.Wait()
}
