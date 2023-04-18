from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, retention_label_settings

from . import entity

class ItemRetentionLabel(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new itemRetentionLabel and sets the default values.
        """
        super().__init__()
        # The isLabelAppliedExplicitly property
        self._is_label_applied_explicitly: Optional[bool] = None
        # The labelAppliedBy property
        self._label_applied_by: Optional[identity_set.IdentitySet] = None
        # The labelAppliedDateTime property
        self._label_applied_date_time: Optional[datetime] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The retentionSettings property
        self._retention_settings: Optional[retention_label_settings.RetentionLabelSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemRetentionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemRetentionLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemRetentionLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, retention_label_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "isLabelAppliedExplicitly": lambda n : setattr(self, 'is_label_applied_explicitly', n.get_bool_value()),
            "labelAppliedBy": lambda n : setattr(self, 'label_applied_by', n.get_object_value(identity_set.IdentitySet)),
            "labelAppliedDateTime": lambda n : setattr(self, 'label_applied_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "retentionSettings": lambda n : setattr(self, 'retention_settings', n.get_object_value(retention_label_settings.RetentionLabelSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_label_applied_explicitly(self,) -> Optional[bool]:
        """
        Gets the isLabelAppliedExplicitly property value. The isLabelAppliedExplicitly property
        Returns: Optional[bool]
        """
        return self._is_label_applied_explicitly
    
    @is_label_applied_explicitly.setter
    def is_label_applied_explicitly(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLabelAppliedExplicitly property value. The isLabelAppliedExplicitly property
        Args:
            value: Value to set for the is_label_applied_explicitly property.
        """
        self._is_label_applied_explicitly = value
    
    @property
    def label_applied_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the labelAppliedBy property value. The labelAppliedBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._label_applied_by
    
    @label_applied_by.setter
    def label_applied_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the labelAppliedBy property value. The labelAppliedBy property
        Args:
            value: Value to set for the label_applied_by property.
        """
        self._label_applied_by = value
    
    @property
    def label_applied_date_time(self,) -> Optional[datetime]:
        """
        Gets the labelAppliedDateTime property value. The labelAppliedDateTime property
        Returns: Optional[datetime]
        """
        return self._label_applied_date_time
    
    @label_applied_date_time.setter
    def label_applied_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the labelAppliedDateTime property value. The labelAppliedDateTime property
        Args:
            value: Value to set for the label_applied_date_time property.
        """
        self._label_applied_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def retention_settings(self,) -> Optional[retention_label_settings.RetentionLabelSettings]:
        """
        Gets the retentionSettings property value. The retentionSettings property
        Returns: Optional[retention_label_settings.RetentionLabelSettings]
        """
        return self._retention_settings
    
    @retention_settings.setter
    def retention_settings(self,value: Optional[retention_label_settings.RetentionLabelSettings] = None) -> None:
        """
        Sets the retentionSettings property value. The retentionSettings property
        Args:
            value: Value to set for the retention_settings property.
        """
        self._retention_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isLabelAppliedExplicitly", self.is_label_applied_explicitly)
        writer.write_object_value("labelAppliedBy", self.label_applied_by)
        writer.write_datetime_value("labelAppliedDateTime", self.label_applied_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("retentionSettings", self.retention_settings)
    

