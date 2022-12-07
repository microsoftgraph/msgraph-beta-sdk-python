from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_action_result = lazy_import('msgraph.generated.models.device_action_result')

class RevokeAppleVppLicensesActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new RevokeAppleVppLicensesActionResult and sets the default values.
        """
        super().__init__()
        # Total number of Apple Vpp licenses that failed to revoke
        self._failed_licenses_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Total number of Apple Vpp licenses associated
        self._total_licenses_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RevokeAppleVppLicensesActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RevokeAppleVppLicensesActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RevokeAppleVppLicensesActionResult()
    
    @property
    def failed_licenses_count(self,) -> Optional[int]:
        """
        Gets the failedLicensesCount property value. Total number of Apple Vpp licenses that failed to revoke
        Returns: Optional[int]
        """
        return self._failed_licenses_count
    
    @failed_licenses_count.setter
    def failed_licenses_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedLicensesCount property value. Total number of Apple Vpp licenses that failed to revoke
        Args:
            value: Value to set for the failedLicensesCount property.
        """
        self._failed_licenses_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "failed_licenses_count": lambda n : setattr(self, 'failed_licenses_count', n.get_int_value()),
            "total_licenses_count": lambda n : setattr(self, 'total_licenses_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("failedLicensesCount", self.failed_licenses_count)
        writer.write_int_value("totalLicensesCount", self.total_licenses_count)
    
    @property
    def total_licenses_count(self,) -> Optional[int]:
        """
        Gets the totalLicensesCount property value. Total number of Apple Vpp licenses associated
        Returns: Optional[int]
        """
        return self._total_licenses_count
    
    @total_licenses_count.setter
    def total_licenses_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalLicensesCount property value. Total number of Apple Vpp licenses associated
        Args:
            value: Value to set for the totalLicensesCount property.
        """
        self._total_licenses_count = value
    

