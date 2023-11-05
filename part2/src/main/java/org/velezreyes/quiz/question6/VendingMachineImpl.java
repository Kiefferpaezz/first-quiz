package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private int money;

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    money += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    switch (name) {
      case "ScottCola":
        if (money >= 75) {
          money -= 75;
          Drink scottCola = new ScottCola("ScottCola", true, "ScottCola is the best!");
          return scottCola;
        } else {
          throw new NotEnoughMoneyException();
        }

      case "KarenTea":
        if (money >= 100) {
          money -= 100;
          Drink karenTea = new KarenTea("KarenTea", false, "karenTea is the best!");
          return karenTea;
        } else {
          throw new NotEnoughMoneyException();
        }

      default:
        throw new UnknownDrinkException();
    }
  }
}
