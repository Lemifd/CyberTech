import asyncio
import socket


async def handle_client(client_reader, client_writer):
    print("New client handling",flush=True)
    # Read the client request with a timeout of 5 seconds
    try:
        request_data = await asyncio.wait_for(client_reader.read(), timeout=5.0)
    except asyncio.TimeoutError:
        print("Timeout while waiting for client request")
        return
    
    # Extract the destination address and port from the request
    destination = request_data.decode().split()[1]
    destination_address = destination.split(':')[0]
    destination_port = int(destination.split(':')[1])
    
    # Forward the request to the destination
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((destination_address, destination_port))
    server_socket.sendall(request_data)
    
    # Read the server response with a timeout of 5 seconds
    try:
        response_data = await asyncio.wait_for(server_socket.recv(4096) ,timeout=20)
    except asyncio.TimeoutError:
        print("Timeout while waiting for server response")
        server_socket.close()
        return 'timeout'
    
    while response_data:
        # Forward the response to the client
        client_writer.write(response_data)
        response_data = server_socket.recv(4096)
    
    # Close the connection to the destination
    server_socket.close()
    
    # Close the connection to the client
    client_writer.close()
async def proxy_server():
    # Create a TCP/IP socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('localhost', 8080))
        server_socket.listen(5)

    except Exception as e:
        print(f"Error creating server socket: {e}")
    
    while True:
        try:
            # Accept a client connection
            client_socket, client_address = await loop.sock_accept(server_socket)
            print(f"New client connection from {client_address}")
            
            # Start a new coroutine to handle the client connection
            client_reader = asyncio.StreamReader()
            client_writer = asyncio.StreamWriter(client_socket, None, client_reader, loop)
            task = asyncio.create_task(handle_client(client_reader, client_writer))
            await task
        except Exception as e:
            print(f"Error in handling client request: {e}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(proxy_server())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()