defmodule Solution do
    def read_integer_from_stdin do
        String.trim(IO.gets "")
            |> String.to_integer
    end

    def print_hello_world do
        IO.puts "Hello World"
    end

    def print_hello_world_n_times(n) when n <= 1 do
        print_hello_world
    end
    def print_hello_world_n_times(n) do
        print_hello_world
        print_hello_world_n_times(n - 1)
    end
end

Solution.read_integer_from_stdin
    |> Solution.print_hello_world_n_times
