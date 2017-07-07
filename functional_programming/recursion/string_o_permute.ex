defmodule Solution do
    def read_integer do
        String.trim(IO.gets "")
            |> String.to_integer
    end

    def read_strings(n) when n > 0 do
        String.trim(IO.gets "")
            |> String.to_charlist
            |> Enum.to_list
            |> permute
            |> IO.puts

        read_strings(n - 1)
    end

    def permute(l) when length(l) == 1 do
        [head | _] = l
        head
    end
    def permute(l) when length(l) == 2 do
        [a | tail_1] = l
        [b | _] = tail_1
        b <> a
    end
    def permute(l) do
        [a | tail_1] = l
        [b | tail_2] = tail_1
        b <> a <> permute(tail_2)
    end
end

Solution.read_integer
    |> Solution.read_strings
