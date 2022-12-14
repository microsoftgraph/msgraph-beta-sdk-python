from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
item_category = lazy_import('msgraph.generated.models.item_category')
picture = lazy_import('msgraph.generated.models.picture')

class Item(entity.Entity):
    @property
    def base_unit_of_measure_id(self,) -> Optional[Guid]:
        """
        Gets the baseUnitOfMeasureId property value. The baseUnitOfMeasureId property
        Returns: Optional[Guid]
        """
        return self._base_unit_of_measure_id
    
    @base_unit_of_measure_id.setter
    def base_unit_of_measure_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the baseUnitOfMeasureId property value. The baseUnitOfMeasureId property
        Args:
            value: Value to set for the baseUnitOfMeasureId property.
        """
        self._base_unit_of_measure_id = value
    
    @property
    def blocked(self,) -> Optional[bool]:
        """
        Gets the blocked property value. The blocked property
        Returns: Optional[bool]
        """
        return self._blocked
    
    @blocked.setter
    def blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the blocked property value. The blocked property
        Args:
            value: Value to set for the blocked property.
        """
        self._blocked = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new item and sets the default values.
        """
        super().__init__()
        # The baseUnitOfMeasureId property
        self._base_unit_of_measure_id: Optional[Guid] = None
        # The blocked property
        self._blocked: Optional[bool] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The gtin property
        self._gtin: Optional[str] = None
        # The inventory property
        self._inventory: Optional[float] = None
        # The itemCategory property
        self._item_category: Optional[item_category.ItemCategory] = None
        # The itemCategoryCode property
        self._item_category_code: Optional[str] = None
        # The itemCategoryId property
        self._item_category_id: Optional[Guid] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The picture property
        self._picture: Optional[List[picture.Picture]] = None
        # The priceIncludesTax property
        self._price_includes_tax: Optional[bool] = None
        # The taxGroupCode property
        self._tax_group_code: Optional[str] = None
        # The taxGroupId property
        self._tax_group_id: Optional[Guid] = None
        # The type property
        self._type: Optional[str] = None
        # The unitCost property
        self._unit_cost: Optional[float] = None
        # The unitPrice property
        self._unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Item:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Item
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Item()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "base_unit_of_measure_id": lambda n : setattr(self, 'base_unit_of_measure_id', n.get_object_value(Guid)),
            "blocked": lambda n : setattr(self, 'blocked', n.get_bool_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "gtin": lambda n : setattr(self, 'gtin', n.get_str_value()),
            "inventory": lambda n : setattr(self, 'inventory', n.get_float_value()),
            "item_category": lambda n : setattr(self, 'item_category', n.get_object_value(item_category.ItemCategory)),
            "item_category_code": lambda n : setattr(self, 'item_category_code', n.get_str_value()),
            "item_category_id": lambda n : setattr(self, 'item_category_id', n.get_object_value(Guid)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(picture.Picture)),
            "price_includes_tax": lambda n : setattr(self, 'price_includes_tax', n.get_bool_value()),
            "tax_group_code": lambda n : setattr(self, 'tax_group_code', n.get_str_value()),
            "tax_group_id": lambda n : setattr(self, 'tax_group_id', n.get_object_value(Guid)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "unit_cost": lambda n : setattr(self, 'unit_cost', n.get_float_value()),
            "unit_price": lambda n : setattr(self, 'unit_price', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def gtin(self,) -> Optional[str]:
        """
        Gets the gtin property value. The gtin property
        Returns: Optional[str]
        """
        return self._gtin
    
    @gtin.setter
    def gtin(self,value: Optional[str] = None) -> None:
        """
        Sets the gtin property value. The gtin property
        Args:
            value: Value to set for the gtin property.
        """
        self._gtin = value
    
    @property
    def inventory(self,) -> Optional[float]:
        """
        Gets the inventory property value. The inventory property
        Returns: Optional[float]
        """
        return self._inventory
    
    @inventory.setter
    def inventory(self,value: Optional[float] = None) -> None:
        """
        Sets the inventory property value. The inventory property
        Args:
            value: Value to set for the inventory property.
        """
        self._inventory = value
    
    @property
    def item_category(self,) -> Optional[item_category.ItemCategory]:
        """
        Gets the itemCategory property value. The itemCategory property
        Returns: Optional[item_category.ItemCategory]
        """
        return self._item_category
    
    @item_category.setter
    def item_category(self,value: Optional[item_category.ItemCategory] = None) -> None:
        """
        Sets the itemCategory property value. The itemCategory property
        Args:
            value: Value to set for the itemCategory property.
        """
        self._item_category = value
    
    @property
    def item_category_code(self,) -> Optional[str]:
        """
        Gets the itemCategoryCode property value. The itemCategoryCode property
        Returns: Optional[str]
        """
        return self._item_category_code
    
    @item_category_code.setter
    def item_category_code(self,value: Optional[str] = None) -> None:
        """
        Sets the itemCategoryCode property value. The itemCategoryCode property
        Args:
            value: Value to set for the itemCategoryCode property.
        """
        self._item_category_code = value
    
    @property
    def item_category_id(self,) -> Optional[Guid]:
        """
        Gets the itemCategoryId property value. The itemCategoryId property
        Returns: Optional[Guid]
        """
        return self._item_category_id
    
    @item_category_id.setter
    def item_category_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the itemCategoryId property value. The itemCategoryId property
        Args:
            value: Value to set for the itemCategoryId property.
        """
        self._item_category_id = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. The number property
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    @property
    def picture(self,) -> Optional[List[picture.Picture]]:
        """
        Gets the picture property value. The picture property
        Returns: Optional[List[picture.Picture]]
        """
        return self._picture
    
    @picture.setter
    def picture(self,value: Optional[List[picture.Picture]] = None) -> None:
        """
        Sets the picture property value. The picture property
        Args:
            value: Value to set for the picture property.
        """
        self._picture = value
    
    @property
    def price_includes_tax(self,) -> Optional[bool]:
        """
        Gets the priceIncludesTax property value. The priceIncludesTax property
        Returns: Optional[bool]
        """
        return self._price_includes_tax
    
    @price_includes_tax.setter
    def price_includes_tax(self,value: Optional[bool] = None) -> None:
        """
        Sets the priceIncludesTax property value. The priceIncludesTax property
        Args:
            value: Value to set for the priceIncludesTax property.
        """
        self._price_includes_tax = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("baseUnitOfMeasureId", self.base_unit_of_measure_id)
        writer.write_bool_value("blocked", self.blocked)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("gtin", self.gtin)
        writer.write_float_value("inventory", self.inventory)
        writer.write_object_value("itemCategory", self.item_category)
        writer.write_str_value("itemCategoryCode", self.item_category_code)
        writer.write_object_value("itemCategoryId", self.item_category_id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_bool_value("priceIncludesTax", self.price_includes_tax)
        writer.write_str_value("taxGroupCode", self.tax_group_code)
        writer.write_object_value("taxGroupId", self.tax_group_id)
        writer.write_str_value("type", self.type)
        writer.write_float_value("unitCost", self.unit_cost)
        writer.write_float_value("unitPrice", self.unit_price)
    
    @property
    def tax_group_code(self,) -> Optional[str]:
        """
        Gets the taxGroupCode property value. The taxGroupCode property
        Returns: Optional[str]
        """
        return self._tax_group_code
    
    @tax_group_code.setter
    def tax_group_code(self,value: Optional[str] = None) -> None:
        """
        Sets the taxGroupCode property value. The taxGroupCode property
        Args:
            value: Value to set for the taxGroupCode property.
        """
        self._tax_group_code = value
    
    @property
    def tax_group_id(self,) -> Optional[Guid]:
        """
        Gets the taxGroupId property value. The taxGroupId property
        Returns: Optional[Guid]
        """
        return self._tax_group_id
    
    @tax_group_id.setter
    def tax_group_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the taxGroupId property value. The taxGroupId property
        Args:
            value: Value to set for the taxGroupId property.
        """
        self._tax_group_id = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def unit_cost(self,) -> Optional[float]:
        """
        Gets the unitCost property value. The unitCost property
        Returns: Optional[float]
        """
        return self._unit_cost
    
    @unit_cost.setter
    def unit_cost(self,value: Optional[float] = None) -> None:
        """
        Sets the unitCost property value. The unitCost property
        Args:
            value: Value to set for the unitCost property.
        """
        self._unit_cost = value
    
    @property
    def unit_price(self,) -> Optional[float]:
        """
        Gets the unitPrice property value. The unitPrice property
        Returns: Optional[float]
        """
        return self._unit_price
    
    @unit_price.setter
    def unit_price(self,value: Optional[float] = None) -> None:
        """
        Sets the unitPrice property value. The unitPrice property
        Args:
            value: Value to set for the unitPrice property.
        """
        self._unit_price = value
    

