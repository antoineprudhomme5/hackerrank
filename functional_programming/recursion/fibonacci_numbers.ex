defmodule Solution do
    def fibonacci(0) do 0 end
    def fibonacci(1) do 1 end
    def fibonacci(n) do
        fibonacci(n-1) + fibonacci(n-2)
    end
end

String.trim(IO.gets "")
    |> String.to_integer
    |> - 1
    |> Solution.fibonacci
    |> IO.puts
