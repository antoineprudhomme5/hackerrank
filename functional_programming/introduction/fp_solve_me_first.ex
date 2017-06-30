defmodule Solution do
    def sum(a, b) do
        a + b
    end

    def read_integer_from_stdin do
        String.trim(IO.gets "")
            |> String.to_integer
    end
end

Solution.sum(Solution.read_integer_from_stdin, Solution.read_integer_from_stdin)
    |> IO.puts
