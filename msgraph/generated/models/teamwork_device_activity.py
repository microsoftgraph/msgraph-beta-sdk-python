from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_active_peripherals = lazy_import('msgraph.generated.models.teamwork_active_peripherals')

class TeamworkDeviceActivity(entity.Entity):
    @property
    def active_peripherals(self,) -> Optional[teamwork_active_peripherals.TeamworkActivePeripherals]:
        """
        Gets the activePeripherals property value. The active peripheral devices attached to the device.
        Returns: Optional[teamwork_active_peripherals.TeamworkActivePeripherals]
        """
        return self._active_peripherals
    
    @active_peripherals.setter
    def active_peripherals(self,value: Optional[teamwork_active_peripherals.TeamworkActivePeripherals] = None) -> None:
        """
        Sets the activePeripherals property value. The active peripheral devices attached to the device.
        Args:
            value: Value to set for the activePeripherals property.
        """
        self._active_peripherals = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDeviceActivity and sets the default values.
        """
        super().__init__()
        # The active peripheral devices attached to the device.
        self._active_peripherals: Optional[teamwork_active_peripherals.TeamworkActivePeripherals] = None
        # Identity of the user who created the device activity document.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device activity document was created.
        self._created_date_time: Optional[datetime] = None
        # Identity of the user who last modified the device activity details.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device activity detail was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user who created the device activity document.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the device activity document.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The UTC date and time when the device activity document was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The UTC date and time when the device activity document was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDeviceActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDeviceActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_peripherals": lambda n : setattr(self, 'active_peripherals', n.get_object_value(teamwork_active_peripherals.TeamworkActivePeripherals)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user who last modified the device activity details.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who last modified the device activity details.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The UTC date and time when the device activity detail was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The UTC date and time when the device activity detail was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("activePeripherals", self.active_peripherals)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

