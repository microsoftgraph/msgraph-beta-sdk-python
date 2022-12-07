from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

kerberos_sign_on_settings = lazy_import('msgraph.generated.models.kerberos_sign_on_settings')
single_sign_on_mode = lazy_import('msgraph.generated.models.single_sign_on_mode')

class OnPremisesPublishingSingleSignOn(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesPublishingSingleSignOn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Kerberos Constrained Delegation settings for applications that use Integrated Window Authentication.
        self._kerberos_sign_on_settings: Optional[kerberos_sign_on_settings.KerberosSignOnSettings] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The preferred single-sign on mode for the application. Possible values are: none, onPremisesKerberos, aadHeaderBased,pingHeaderBased.
        self._single_sign_on_mode: Optional[single_sign_on_mode.SingleSignOnMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesPublishingSingleSignOn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishingSingleSignOn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesPublishingSingleSignOn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "kerberos_sign_on_settings": lambda n : setattr(self, 'kerberos_sign_on_settings', n.get_object_value(kerberos_sign_on_settings.KerberosSignOnSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "single_sign_on_mode": lambda n : setattr(self, 'single_sign_on_mode', n.get_enum_value(single_sign_on_mode.SingleSignOnMode)),
        }
        return fields
    
    @property
    def kerberos_sign_on_settings(self,) -> Optional[kerberos_sign_on_settings.KerberosSignOnSettings]:
        """
        Gets the kerberosSignOnSettings property value. The Kerberos Constrained Delegation settings for applications that use Integrated Window Authentication.
        Returns: Optional[kerberos_sign_on_settings.KerberosSignOnSettings]
        """
        return self._kerberos_sign_on_settings
    
    @kerberos_sign_on_settings.setter
    def kerberos_sign_on_settings(self,value: Optional[kerberos_sign_on_settings.KerberosSignOnSettings] = None) -> None:
        """
        Sets the kerberosSignOnSettings property value. The Kerberos Constrained Delegation settings for applications that use Integrated Window Authentication.
        Args:
            value: Value to set for the kerberosSignOnSettings property.
        """
        self._kerberos_sign_on_settings = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("kerberosSignOnSettings", self.kerberos_sign_on_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("singleSignOnMode", self.single_sign_on_mode)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def single_sign_on_mode(self,) -> Optional[single_sign_on_mode.SingleSignOnMode]:
        """
        Gets the singleSignOnMode property value. The preferred single-sign on mode for the application. Possible values are: none, onPremisesKerberos, aadHeaderBased,pingHeaderBased.
        Returns: Optional[single_sign_on_mode.SingleSignOnMode]
        """
        return self._single_sign_on_mode
    
    @single_sign_on_mode.setter
    def single_sign_on_mode(self,value: Optional[single_sign_on_mode.SingleSignOnMode] = None) -> None:
        """
        Sets the singleSignOnMode property value. The preferred single-sign on mode for the application. Possible values are: none, onPremisesKerberos, aadHeaderBased,pingHeaderBased.
        Args:
            value: Value to set for the singleSignOnMode property.
        """
        self._single_sign_on_mode = value
    

