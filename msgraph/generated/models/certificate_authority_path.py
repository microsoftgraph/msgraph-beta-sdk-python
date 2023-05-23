from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_based_application_configuration, entity

from . import entity

class CertificateAuthorityPath(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new certificateAuthorityPath and sets the default values.
        """
        super().__init__()
        # The certificateBasedApplicationConfigurations property
        self._certificate_based_application_configurations: Optional[List[certificate_based_application_configuration.CertificateBasedApplicationConfiguration]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def certificate_based_application_configurations(self,) -> Optional[List[certificate_based_application_configuration.CertificateBasedApplicationConfiguration]]:
        """
        Gets the certificateBasedApplicationConfigurations property value. The certificateBasedApplicationConfigurations property
        Returns: Optional[List[certificate_based_application_configuration.CertificateBasedApplicationConfiguration]]
        """
        return self._certificate_based_application_configurations
    
    @certificate_based_application_configurations.setter
    def certificate_based_application_configurations(self,value: Optional[List[certificate_based_application_configuration.CertificateBasedApplicationConfiguration]] = None) -> None:
        """
        Sets the certificateBasedApplicationConfigurations property value. The certificateBasedApplicationConfigurations property
        Args:
            value: Value to set for the certificate_based_application_configurations property.
        """
        self._certificate_based_application_configurations = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CertificateAuthorityPath:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthorityPath
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CertificateAuthorityPath()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_based_application_configuration, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateBasedApplicationConfigurations": lambda n : setattr(self, 'certificate_based_application_configurations', n.get_collection_of_object_values(certificate_based_application_configuration.CertificateBasedApplicationConfiguration)),
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
        writer.write_collection_of_object_values("certificateBasedApplicationConfigurations", self.certificate_based_application_configurations)
    

