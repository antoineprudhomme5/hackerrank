defmodule Solution do
    def read_integer do
        String.trim(IO.gets "")
            |> String.to_integer
    end

    def print_unicode_list(l) do
        Enum.map(l, fn x -> <<x :: utf8>> end)
            |> Enum.reduce(fn(x, acc) -> x <> acc end)
            |> IO.puts
    end

    def read_strings(n) when n > 0 do
        String.trim(IO.gets "")
            |> String.to_charlist
            |> Enum.to_list
            |> permute
            |> print_unicode_list

        read_strings(n - 1)
    end

    def permute(l) when length(l) == 1 do
        [List.first(l)]
    end
    def permute(l) when length(l) == 2 do
        [List.last(l), List.first(l)]
    end
    def permute(l) do
        splitted = Enum.split(l, 2)
        a = List.first(elem(splitted, 0))
        b = List.last(elem(splitted, 0))
        [b, a] permute(elem(splitted, 1))
    end
end

Solution.read_integer
    |> Solution.read_strings
