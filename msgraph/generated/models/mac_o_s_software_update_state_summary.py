from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mac_o_s_software_update_category = lazy_import('msgraph.generated.models.mac_o_s_software_update_category')
mac_o_s_software_update_state = lazy_import('msgraph.generated.models.mac_o_s_software_update_state')

class MacOSSoftwareUpdateStateSummary(entity.Entity):
    """
    MacOS software update state summary for a device and user
    """
    def __init__(self,) -> None:
        """
        Instantiates a new macOSSoftwareUpdateStateSummary and sets the default values.
        """
        super().__init__()
        # Human readable name of the software update
        self._display_name: Optional[str] = None
        # Last date time the report for this device and product key was updated.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Product key of the software update.
        self._product_key: Optional[str] = None
        # MacOS Software Update State
        self._state: Optional[mac_o_s_software_update_state.MacOSSoftwareUpdateState] = None
        # MacOS Software Update Category
        self._update_category: Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory] = None
        # Version of the software update
        self._update_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSoftwareUpdateStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSSoftwareUpdateStateSummary()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Human readable name of the software update
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Human readable name of the software update
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "product_key": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(mac_o_s_software_update_state.MacOSSoftwareUpdateState)),
            "update_category": lambda n : setattr(self, 'update_category', n.get_enum_value(mac_o_s_software_update_category.MacOSSoftwareUpdateCategory)),
            "update_version": lambda n : setattr(self, 'update_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Last date time the report for this device and product key was updated.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Last date time the report for this device and product key was updated.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def product_key(self,) -> Optional[str]:
        """
        Gets the productKey property value. Product key of the software update.
        Returns: Optional[str]
        """
        return self._product_key
    
    @product_key.setter
    def product_key(self,value: Optional[str] = None) -> None:
        """
        Sets the productKey property value. Product key of the software update.
        Args:
            value: Value to set for the productKey property.
        """
        self._product_key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("productKey", self.product_key)
        writer.write_enum_value("state", self.state)
        writer.write_enum_value("updateCategory", self.update_category)
        writer.write_str_value("updateVersion", self.update_version)
    
    @property
    def state(self,) -> Optional[mac_o_s_software_update_state.MacOSSoftwareUpdateState]:
        """
        Gets the state property value. MacOS Software Update State
        Returns: Optional[mac_o_s_software_update_state.MacOSSoftwareUpdateState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[mac_o_s_software_update_state.MacOSSoftwareUpdateState] = None) -> None:
        """
        Sets the state property value. MacOS Software Update State
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def update_category(self,) -> Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory]:
        """
        Gets the updateCategory property value. MacOS Software Update Category
        Returns: Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory]
        """
        return self._update_category
    
    @update_category.setter
    def update_category(self,value: Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory] = None) -> None:
        """
        Sets the updateCategory property value. MacOS Software Update Category
        Args:
            value: Value to set for the updateCategory property.
        """
        self._update_category = value
    
    @property
    def update_version(self,) -> Optional[str]:
        """
        Gets the updateVersion property value. Version of the software update
        Returns: Optional[str]
        """
        return self._update_version
    
    @update_version.setter
    def update_version(self,value: Optional[str] = None) -> None:
        """
        Sets the updateVersion property value. Version of the software update
        Args:
            value: Value to set for the updateVersion property.
        """
        self._update_version = value
    

