class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # il y aura exactement 1 reine par ligne et par colonne
        output: list[list[str]] = []
        res: list[str] = []

        def get_slots(res: Optional[list[str]]) -> list[int]:
            """
            Renvoie les slots disponibles pour la i+1-ème ligne sachant la position des reines au dessus
            """
            i = len(res)
            slots: list[int] = [k for k in range(n)] # on initialise les slots comme valides partout
            if not res:
                return slots
            for index_row, row in enumerate(res):
                for position, queen in enumerate(row):
                    if queen == "Q":
                        try:
                            slots.remove(position) # on retire la ligne position car en joug de cette reine
                        except ValueError:
                            pass
                        if position + i - index_row <= n:
                            try:
                                slots.remove(position + i - index_row) # on retire la ligne position car en joug de cette reine
                            except ValueError:
                                pass
                        if position - i + index_row >= 0:
                            try:
                                slots.remove(position - i + index_row) # on retire la ligne position car en joug de cette reine
                            except ValueError:
                                pass
            return slots

        def backtrack(i: int) -> None:
            # Il n'y a pas de slots ou placer la reine
            slots: list[int] = get_slots(res)
            if i == n:
                output.append(res.copy())
                return
            if not slots:
                return
            else:
                for slot in slots:
                    if slot == 0:
                        res.append("Q" + "." * (n-1))
                    elif slot == n-1:
                        res.append("." * (n-1) + "Q")
                    else:
                        res.append("." * slot + "Q" + "." * (n-slot-1))
                    backtrack(i+1)
                    res.pop()

        backtrack(0)
        return output