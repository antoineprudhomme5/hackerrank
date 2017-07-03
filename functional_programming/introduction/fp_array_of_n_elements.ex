defmodule Solution do
    def generate_list(l) do
        Enum.to_list 1..l
    end
    def print_list(l) do
         IO.puts("[#{Enum.join(l, ", ")}]")
    end
end

String.trim(IO.gets "")
    |> String.to_integer
    |> Solution.generate_list
    |> Solution.print_list
